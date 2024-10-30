variable "project_id" {
  default = "globantchallenge-440021"
  type = string
}
variable "region" { 
  default = "us-central1"
  type = string
}
variable "github_owner" {
  default = "ludsonfelipe"
  type = string
}
variable "github_repo" {
  default = "globant_challenge"
  type = string
}
variable "artifact_registry_repository" {
  default = "gcr-repository"
  type = string
}
variable "app_name" {
  default = "apiglobantchallenge"
  type = string
}