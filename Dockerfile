# ─────────────────────────────────────────
# Step 1: Start from Alpine Linux (minimal base ~5MB)
# ─────────────────────────────────────────
FROM alpine:3.19

# ─────────────────────────────────────────
# Step 2: Install Python + pip + build tools
# Alpine uses apk as its package manager
# --no-cache avoids storing the index locally (keeps image small)
# ─────────────────────────────────────────
RUN apk add --no-cache \
    python3 \
    py3-pip \
    build-base \
    curl \
    pkgconfig \
    python3-dev \
    freetype-dev \
    libpng-dev \
    gdal-dev

# ─────────────────────────────────────────
# Step 3: Set up the working directory
# This is where our app will live inside the container
# ─────────────────────────────────────────
WORKDIR /app

# ─────────────────────────────────────────
# Step 4: Create and activate a virtual environment
# Best practice on Alpine to avoid system pip conflicts
# ─────────────────────────────────────────
RUN python3 -m venv /app/venv
ENV PATH="/app/venv/bin:$PATH"

# ─────────────────────────────────────────
# Step 5: Copy requirements and install packages
# We copy requirements FIRST (before app code)
# so Docker can cache this layer — reinstall only when requirements change
# ─────────────────────────────────────────
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ─────────────────────────────────────────
# Step 6: Copy the application code
# Done last so code changes don't bust the pip cache layer
# ─────────────────────────────────────────
COPY app/ .

# ─────────────────────────────────────────
# Step 7: Expose the Streamlit default port
# ─────────────────────────────────────────
EXPOSE 8501
# ─────────────────────────────────────────
# Step 8: Run Streamlit
# --server.address=0.0.0.0 makes it reachable outside the container
# --server.headless=true   disables the browser auto-open prompt
# ─────────────────────────────────────────
CMD ["streamlit", "run", "app.py", \
     "--server.port=8501", \
     "--server.address=0.0.0.0", \
     "--server.headless=true"]
