resource "aws_key_pair" "example" {
  key_name   = "id_rsa"
  public_key = file("/home/alegaz/.ssh/id_rsa.pub")
}

resource "aws_instance" "example" {
  ami           = "ami-0c55b159cbfafe1f0"  # ID de la AMI de Ubuntu
  instance_type = "t2.micro"
  key_name      = aws_key_pair.example.key_name

  tags = {
    Name = "ExampleInstance"
  }

  vpc_security_group_ids = [aws_security_group.instance_sg.id]
}