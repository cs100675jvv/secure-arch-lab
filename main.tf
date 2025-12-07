provider "aws" {
  region = "us-east-1"
}

resource "aws_security_group" "user_api" {
  name        = "user-api-sg"
  description = "Allow 443 from anywhere"

  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]  # ❌ відкрита зона
  }
}
