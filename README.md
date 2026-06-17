# Media Extractor

A high-performance Python automation tool designed to optimize media processing pipelines on multi-core systems. The script concurrently splits video files into independent audio tracks and extracts visual mid-point thumbnails.

## Core Architecture & Concepts
* **Thread-Level Concurrency:** Utilizes `ThreadPoolExecutor` mapped across 4 worker threads to maximize CPU utilization on 4-core hardware setups without context-switching bloat. Rather than using `Pool` (which duplicates the whole Python process in memory) using `ThreadPoolExecutor` and leting `ffmpeg` do all the heavy lifting and actual rendering in its own isolated OS processes
* **Subprocess Interleaving:** Decouples heavy rendering tasks from the main Python thread by spawning native, isolated `ffmpeg` forks via the `subprocess` module.
* **Dynamic Frame Extraction:** Leverages `moviepy` metadata calculation to compute video durations dynamically, allowing `ffmpeg` to seek precisely (`-ss`) to the mathematical midpoint of any container format.

##  How It Works
1. **Directory Scanning:** Maps the target filesystem using standard I/O streams.
2. **Worker Allocation:** Feeds the file array into a thread pool worker queue.
3. **Extraction Pipeline:** * Thread extracts audio without re-encoding (`-c:a copy`).
   * Thread seeking logic extracts exactly 1 frame (`-frames:v 1`) at `duration // 2` to create a preview thumbnail.

## Requirements
1. **FFmpeg:** Requires proper `ffmpeg` installation added to your system's PATH.
2. **Python:** `Python` 3.x or higher.
3. **External Libraries:** Requires `moviepy` for video metadata calculations.
