FROM python:3.11-slim

WORKDIR /app
RUN pip install uv

# Copy only dependency files first
COPY pyproject.toml uv.lock* ./
RUN uv sync --no-dev --frozen

# Copy only required source files
COPY main.py tools.py ./

EXPOSE 8000

CMD ["uv", "run", "main.py"]
