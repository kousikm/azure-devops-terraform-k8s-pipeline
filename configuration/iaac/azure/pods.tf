resource "kubernetes_pod" "test" {
  metadata {
    name = "terraform-example"
  }

  spec {
    container {
      image = "kousikm/hello_rest_api"
      name  = "hello_api_container"
    }
  }
}
