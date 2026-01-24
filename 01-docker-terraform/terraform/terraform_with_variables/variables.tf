variable "project" {
  description = "Project"
  default     = "massive-cirrus-412608"
}

variable "credentials" {
  description = "Project Credentials"
  default     = "../keys/terraform-runner-keys.json"
  #ex: if you have a directory where this file is called keys with your service account json file
  #saved there as my-creds.json you could use default = "./keys/my-creds.json"
}

variable "region" {
  description = "Project Region"
  #Update the below to your desired region
  default     = "us-central1"
}

variable "location" {
  description = "Project Location"
  #Update the below to your desired location
  default     = "US"
}

variable "bq_dataset_name" {
  description = "Project BigQuery Dataset Name"
  #Update the below to what you want your dataset to be called
  default     = "demo_dataset"
}

variable "gcs_bucket_name" {
  description = "Project Storage Bucket Name"
  #Update the below to a unique bucket name
  default     = "terraform-demo-data-bucket"
}

variable "gcs_storage_class" {
  description = "Project Bucket Storage Class"
  default     = "STANDARD"
}