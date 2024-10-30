provider "google" {
  credentials = file("./gcp_key/key.json")
  project     = var.project_id
  region      = var.region
}

provider "google-beta" {
  credentials = file("./gcp_key/key.json")
  project     = var.project_id
  region      = var.region
}

module "project-services" {
  source                      = "terraform-google-modules/project-factory/google//modules/project_services"
  version                     = "17.0.0"
  disable_services_on_destroy = false

  project_id  = var.project_id
  enable_apis = true

  activate_apis = [
    "serviceusage.googleapis.com",
    "cloudresourcemanager.googleapis.com",
    "iam.googleapis.com",
    "run.googleapis.com",
    "cloudbuild.googleapis.com",
    "servicemanagement.googleapis.com",
  ]
}

resource "google_service_account" "cloudbuild_service_account" {
  account_id   = "cloudbuild-sa"
  display_name = "cloudbuild-sa"
  description  = "Cloud build service account"
}

resource "google_project_iam_member" "act_as" {
  project = var.project_id
  role    = "roles/iam.serviceAccountUser"
  member  = "serviceAccount:${google_service_account.cloudbuild_service_account.email}"
}

resource "google_project_iam_member" "logs_writer" {
  project = var.project_id
  role    = "roles/logging.logWriter"
  member  = "serviceAccount:${google_service_account.cloudbuild_service_account.email}"
}

resource "google_project_iam_member" "artifactregistry_admin" {
  project = var.project_id
  role    = "roles/artifactregistry.admin"
  member  = "serviceAccount:${google_service_account.cloudbuild_service_account.email}"
}

resource "google_project_iam_member" "cloudrun_admin" {
  project = var.project_id
  role    = "roles/run.admin"
  member  = "serviceAccount:${google_service_account.cloudbuild_service_account.email}"
}

module "artifact_registry" {
  source = "./artifact_registry"
  region = var.region
  repository_id = var.artifact_registry_repository
}

module "cloud_build" {
  source = "./cloud_build"
  github_owner = var.github_owner
  app_name = var.app_name
  github_repo = var.github_repo
  project_id = var.project_id
  region = var.region
  service_account = google_service_account.cloudbuild_service_account.id
  artifact_registry_repository = var.artifact_registry_repository
  depends_on = [ google_project_iam_member.act_as, 
    google_project_iam_member.logs_writer, 
    google_project_iam_member.artifactregistry_admin, 
    google_project_iam_member.cloudrun_admin, 
    google_service_account.cloudbuild_service_account,
    module.artifact_registry
  ]
}
