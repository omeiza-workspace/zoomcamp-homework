terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.6.0"
    }
  }
}

provider "google" {
  credentials = file(var.credentials)
  project     = var.project
  region      = var.region
}


# -----------------------------
# Google Cloud Storage Bucket
# -----------------------------
resource "google_storage_bucket" "data_bucket" {
  name                        = var.gcs_bucket_name
  location                    = var.region
  storage_class               = var.gcs_storage_class
  uniform_bucket_level_access = true
  force_destroy               = true

  versioning {
    enabled = true
  }

  lifecycle_rule {
    action {
      type = "AbortIncompleteMultipartUpload"
    }
    condition {
      age = 1
    }
  }

  labels = {
    env  = "dev"
    team = "data"
  }
}

# -----------------------------
# BigQuery Dataset
# -----------------------------
resource "google_bigquery_dataset" "dataset" {
  dataset_id = var.bq_dataset_name
  project    = var.project
  location   = var.location

  description = "Dataset for demo data created via Terraform"
  labels = {
    env  = "dev"
    team = "data"
  }
}