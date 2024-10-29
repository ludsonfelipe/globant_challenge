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
  ]
}

resource "google_cloud_run_service" "fastapi_service" {
  name     = "fastapi-api"
  location = var.region

  template {
    spec {
      containers {
        image = "gcr.io/${var.project_id}/fastapi-api:latest"
      }
    }
  }

  depends_on = [ module.project-services ]
}

