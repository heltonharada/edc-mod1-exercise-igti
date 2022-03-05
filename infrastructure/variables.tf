variable "aws_region" {
  default = "us-east-1"
}

#criação de nova variável para o Use case 1 - Lakehouse com DeltaLake e EMR

variable "lambda_function_name" {
  default = "IGTIexecutaEMR"  
}

#criação de novas variáveis para o Use case 3 - Pipelines com Airflow

variable "key_pair_name" {
  default = "helton-igti-teste"
}

variable "airflow_subnet_id" {
  default = "subnet-07d733f7233d60f1b"
}

variable "vpc_id" {
  default = "vpc-0cd132980d503447a"
}