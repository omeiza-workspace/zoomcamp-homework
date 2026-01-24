# Start with slim Python 3.13 image
FROM python:3.13-slim

# Copy uv binary from official uv image (multi-stage build pattern)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

# Set working directory
WORKDIR /app

# Enable bytecode compilation for faster execution and smaller image size
ENV UV_COMPILE_BYTECODE=1

# Copy dependency files first (better layer caching)
# We copy these BEFORE the code so we don't re-install libs every time we edit the script
COPY "pyproject.toml" "uv.lock" ".python-version" ./

# Install dependencies from lock file (ensures reproducible builds)
# We use --frozen to ensure the lockfile isn't updated during build
# RUN uv sync --frozen --no-install-project
RUN uv add pandas sqlalchemy psycopg2-binary pyarrow click tqdm

RUN mkdir -p /app/data
COPY data/ /app/data/

# Copy application code
COPY ingest_data.py .

# Add virtual environment to PATH so we can use installed packages
# 'uv sync' creates the .venv in the WORKDIR (/app)
ENV PATH="/app/.venv/bin:$PATH"

# Set entry point
ENTRYPOINT ["python", "ingest_data.py"]
