docker run \
    -v $(pwd)/litellm_config.yaml:/app/config.yaml \
    -e OPENAI_API_KEY= \
    -p 4000:4000 \
    ghcr.io/berriai/litellm:main-stable \
    --config /app/config.yaml --detailed_debug
