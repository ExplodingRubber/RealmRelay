Write-Host "Installing RealmRelay prerequisites..." -ForegroundColor Cyan

# Check Python
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "Python was not found. Please install Python 3.12+ first." -ForegroundColor Red
    exit 1
}

Write-Host "Python detected:"
python --version

# Create virtual environment if missing
if (-not (Test-Path ".\.venv")) {
    Write-Host "Creating Python virtual environment..." -ForegroundColor Yellow
    python -m venv .venv
}
else {
    Write-Host "Virtual environment already exists." -ForegroundColor Green
}

# Activate environment
Write-Host "Installing Python packages..." -ForegroundColor Yellow

& ".\.venv\Scripts\python.exe" -m pip install --upgrade pip

& ".\.venv\Scripts\pip.exe" install `
    fastapi `
    uvicorn `
    psutil `
    pydantic

Write-Host ""
Write-Host "RealmRelay prerequisites installed successfully!" -ForegroundColor Green
Write-Host ""
Write-Host "To start development:"
Write-Host ".\.venv\Scripts\Activate.ps1"