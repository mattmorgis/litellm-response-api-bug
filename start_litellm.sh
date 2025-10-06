docker run \
    -v $(pwd)/litellm_config.yaml:/app/config.yaml \
    -e AZURE_API_KEY= \
    -p 4000:4000 \
    ghcr.io/berriai/litellm:v1.77.5-stable \
    --config /app/config.yaml --detailed_debug
