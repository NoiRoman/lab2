# ci.ps1 — Скрипт непрерывной интеграции (Continuous Integration)
# Проект: Calculator
# Автор: РоманКубаткин
# Дата: 11.09.2026

$ErrorActionPreference = "Stop"
$RepoDir = "C:\Users\kubat\OneDrive\Рабочий стол\lab2"
$InnoSetupCompiler = "C:\Program Files (x86)\Inno Setup 6\ISCC.exe"
$InstallerOutputDir = "C:\Users\kubat\OneDrive\Рабочий стол\lab2\installer"


function Write-Step($message) {
    Write-Host ""
    Write-Host "=====================================================" -ForegroundColor Cyan
    Write-Host "  $message" -ForegroundColor Cyan
    Write-Host "=====================================================" -ForegroundColor Cyan
}

function Write-Ok($message) {
    Write-Host "  [OK] $message" -ForegroundColor Green
}

function Write-Err($message) {
    Write-Host "  [ERROR] $message" -ForegroundColor Red
}


Write-Host ""
Write-Host "  CI-скрипт для проекта Calculator" -ForegroundColor Yellow
Write-Host "  Начало: $(Get-Date)" -ForegroundColor Yellow


Write-Step "Шаг 1/5: Загрузка актуального состояния с сервера"

Set-Location $RepoDir

git checkout main
git pull origin main

if ($LASTEXITCODE -ne 0) {
    Write-Err "Не удалось загрузить обновления с GitHub"
    exit 1
}
Write-Ok "Актуальное состояние загружено"


Write-Step "Шаг 2/5: Сборка проекта (PyInstaller)"

py -m pip show pyinstaller > $null 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "  Устанавливаю PyInstaller..." -ForegroundColor Yellow
    py -m pip install pyinstaller
}

py -m PyInstaller --onefile --noconsole --name Calculator main.py

if ($LASTEXITCODE -ne 0) {
    Write-Err "Ошибка сборки .exe через PyInstaller"
    exit 1
}

if (-not (Test-Path ".\dist\Calculator.exe")) {
    Write-Err "Файл dist\Calculator.exe не создан!"
    exit 1
}
Write-Ok "Проект собран: dist\Calculator.exe"


Write-Step "Шаг 3/5: Запуск unit-тестов"

py test_lab2.py

if ($LASTEXITCODE -ne 0) {
    Write-Err "Unit-тесты провалены! Сборка прервана."
    exit 1
}
Write-Ok "Все unit-тесты пройдены"


Write-Step "Шаг 4/5: Создание установщика через Inno Setup"

if (-not (Test-Path $InnoSetupCompiler)) {
    Write-Err "Inno Setup Compiler не найден: $InnoSetupCompiler"
    exit 1
}

& $InnoSetupCompiler "installer.iss"

if ($LASTEXITCODE -ne 0) {
    Write-Err "Ошибка компиляции installer.iss"
    exit 1
}

$installerPath = Join-Path $InstallerOutputDir "Calculator_Setup.exe"
if (-not (Test-Path $installerPath)) {
    Write-Err "Файл установщика не найден: $installerPath"
    exit 1
}
Write-Ok "Установщик создан: $installerPath"


Write-Step "Шаг 5/5: Тихая установка приложения"

Start-Process -FilePath $installerPath -ArgumentList "/SILENT", "/SUPPRESSMSGBOXES", "/NORESTART" -Wait

Write-Ok "Приложение установлено"

$installedPath = "C:\Program Files\Calculator\Calculator.exe"
if (Test-Path $installedPath) {
    Write-Ok "Приложение найдено по пути: $installedPath"
} else {
    Write-Host "  Проверьте путь установки вручную" -ForegroundColor Yellow
}


Write-Host ""
Write-Host "=====================================================" -ForegroundColor Green
Write-Host "  CI-процесс успешно завершён!" -ForegroundColor Green
Write-Host "  Конец: $(Get-Date)" -ForegroundColor Green
Write-Host "=====================================================" -ForegroundColor Green