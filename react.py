import subprocess


def start_nextjs_dev_server():
    # Replace with your Next.js project directory
    nextjs_dir = '/web-file-system'
    # Run the Next.js development server
    subprocess.run(['npm', 'run', 'dev'], cwd=nextjs_dir)