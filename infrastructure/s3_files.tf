# atualizando forma de declarar recursos conforme nova versão do Terraform:
# https://registry.terraform.io/providers/hashicorp/aws/latest/docs/guides/version-4-upgrade)

# resource "aws_s3_bucket_object" "job_spark" {
resource "aws_s3_object" "job_spark" {
  # bucket = aws_s3_bucket.datalake.id
  bucket = aws_s3_bucket.dl.id

  key    = "emr-code/pyspark/job_spark_from_tf.py"
  acl    = "private"
  source = "../job_spark.py"
  etag   = filemd5("../job_spark.py")

}