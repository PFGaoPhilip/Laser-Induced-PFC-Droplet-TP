param([Parameter(Mandatory=$true)][string]$JobFile)
$ErrorActionPreference = 'Stop'
$jobs = Get-Content -LiteralPath $JobFile -Raw | ConvertFrom-Json
$results = @()
foreach ($job in $jobs) {
    $powerPoint = New-Object -ComObject PowerPoint.Application
    try {
        $source = [System.IO.Path]::GetFullPath($job.pptx)
        $output = [System.IO.Path]::GetFullPath($job.output)
        [System.IO.Directory]::CreateDirectory($output) | Out-Null
        $presentation = $powerPoint.Presentations.Open($source, $true, $false, $false)
        try {
            $width = 1600
            $height = [int][math]::Round($width * $presentation.PageSetup.SlideHeight / $presentation.PageSetup.SlideWidth)
            $indices = if ($job.PSObject.Properties['slides']) { @($job.slides) } else { @(1..$presentation.Slides.Count) }
            foreach ($slideIndexValue in $indices) {
                $slideIndex = [int]$slideIndexValue
                $slide = $presentation.Slides.Item($slideIndex)
                try {
                    $filename = Join-Path $output ('slide-{0:d3}.png' -f $slideIndex)
                    $slide.Export($filename, 'PNG', $width, $height)
                } finally { [System.Runtime.InteropServices.Marshal]::FinalReleaseComObject($slide) | Out-Null }
            }
            $results += @{pptx=$source; output=$output; slides=$presentation.Slides.Count; exported_slides=$indices; width=$width; height=$height; renderer='Microsoft PowerPoint'; status='rendered; visual inspection pending'}
            Write-Output ('Rendered {0} slides: {1}' -f $presentation.Slides.Count, $source)
        } finally {
            $presentation.Close()
            [System.Runtime.InteropServices.Marshal]::FinalReleaseComObject($presentation) | Out-Null
        }
    } finally {
        $powerPoint.Quit()
        [System.Runtime.InteropServices.Marshal]::FinalReleaseComObject($powerPoint) | Out-Null
        [GC]::Collect()
        [GC]::WaitForPendingFinalizers()
    }
}
$report = [System.IO.Path]::ChangeExtension([System.IO.Path]::GetFullPath($JobFile), '.rendered.json')
ConvertTo-Json -InputObject @($results) -Depth 5 | Set-Content -LiteralPath $report -Encoding utf8
