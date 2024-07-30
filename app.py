from moviepy import editor as mp
import click
from pathlib import Path

@click.group()
def cli():
    pass

# Cut command
@cli.command('cut')
@click.argument('video_path', type=click.Path(exists=True))
@click.argument('start_time', type=str)
@click.argument('end_time', type=str)
@click.argument('final_name', type=str, default="trimmed_video", required=False)
def cut(video_path, start_time, end_time, final_name):
    """Cut a video from start_time to end_time."""
    video = mp.VideoFileClip(video_path)
    video_clip = video.subclip(start_time, end_time)

    # Get file extension and create output path
    file_extension = Path(video_path).suffix
    output_path = Path(final_name).with_suffix(file_extension)

    video_clip.write_videofile(output_path)

# Convert command
@cli.command('convert')
@click.argument('video_path', type=click.Path(exists=True))
@click.argument('format_to_convert', type=str)
@click.argument('final_name', type=str, default="video_converted", required=False)
def convert(video_path, format_to_convert, final_name):
    """Convert a video to a specified format."""
    video = mp.VideoFileClip(video_path)

    # Create output path with new format
    output_path = Path(final_name).with_suffix(f".{format_to_convert}")

    video.write_videofile(output_path)

if __name__ == '__main__':
    cli()
