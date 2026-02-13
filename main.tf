# Configure the AWS provider
provider "aws" {
  region = "eu-west-1"
}

# Create a S3 bucket
resource "aws_s3_bucket" "terraform_state" {
  bucket		  = "${var.bucket_name}"
  
  versioning {
    enabled = true
  }  
  
  lifecycle {
    prevent_destroy = true
  }
}

resource "aws_s3_bucket_public_access_block" "insecure" {
  bucket = aws_s3_bucket.terraform_state.id

  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false
}
