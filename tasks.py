import click

from bms_data_streamer.resources import sensor_readings_generator
from bms_data_streamer.sender import send_sensors_data

cli = click.Group()


@cli.command()
def generate():
    """
    Generates sensors readings files
    """
    sensor_readings_generator.generate_sensor_readings_files()


@cli.command()
def send():
    """
    Streams the data from sensors to console
    """
    send_sensors_data()


if __name__ == '__main__':
    cli()
