provider "aws" {
  region = "us-east-2"
  profile = "default"
}

terraform {
  backend "s3" {
    bucket = "morgantho-terraform-state"
    key = "resume-site.tfstate"
    region = "us-east-2"
    dynamodb_table = "terraform-state"
  }
}

module "dynamodb" {
  source = "github.com/morgantho/terraform/modules/dynamodb"

  table_name = "site_count"
  hash_key = "Site"
  billing = "PAY_PER_REQUEST"
  attribute_name = "Site"
  attribute_type = "N"
}
