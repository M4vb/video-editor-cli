import moviepy.editor as mp
import click


@click.group()
def cli():
    pass


# Cut command
@cli.command('cut')
@click.argument('video_name', type=click.Path(exists=True))
@click.argument('start_time', type=str)
@click.argument('end_time', type=str)
@click.argument('final_name', type=str, default="trimmed video", required=False)
def cut(video_name, start_time, end_time, final_name):
    file_extension = video_name.split('.')[-1]

    video = mp.VideoFileClip(video_name)
    video_clip = video.subclip(start_time, end_time)

    video_clip.write_videofile(f"{final_name}.{file_extension}")


# Convert Command
@cli.command('convert')
@click.argument('video_name', type=click.Path(exists=True))
@click.argument('format_to_convert', type=str)
@click.argument('final_name', type=str, default="video_converted", required=False)
def convertir(video_name, format_to_convert, final_name):
    video = mp.VideoFileClip(video_name)
    video.write_videofile(f"{final_name}.{format_to_convert}")


if __name__ == '__main__':
    cli()
