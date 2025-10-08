#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let (mut health_reporter, health_service) = tonic_health::server::health_reporter();
    health_reporter
        .set_service_status("".to_string(), tonic_health::ServingStatus::Serving)
        .await;

    let addr = "0.0.0.0:50051".parse().unwrap();

    tonic::transport::Server::builder()
        .add_service(health_service)
        .serve(addr)
        .await?;

    Ok(())
}

