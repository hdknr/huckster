#!/usr/bin/env python
import click
import os
import importlib.util

BIN = os.path.dirname(os.path.abspath(__file__))


def bin_file(name):
    return os.path.join(BIN, name)


def import_settings(path=None):
    path = path or os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        'web/app/local_settings.py')
    spec = importlib.util.spec_from_file_location("local_settings", path)
    settings = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(settings)
    return settings


@click.group()
def db():
    pass


@db.command()
@click.option('--database', '-d', default='default')
@click.option('--path', '-p', default=None)
def createdb(database, path):
    settings = import_settings(path)
    SCRIPT = '''CREATE DATABASE {NAME}
DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
GRANT ALL on {NAME}.*
to '{USER}'@'{HOST}'
identified by '{PASSWORD}' WITH GRANT OPTION; '''
    print(SCRIPT.format(**settings.DATABASES[database]))


@db.command()
@click.option('--database', '-d', default='default')
@click.option('--path', '-p', default=None)
def dumpschema(database, path):
    settings = import_settings(path)
    CMD = 'mysqldump -u {USER} --password={PASSWORD} -h {HOST} {NAME} -d'
    print(CMD.format(**settings.DATABASES[database]))


@db.command()
@click.option('--database', '-d', default='default')
@click.option('--path', '-p', default=None)
@click.option('--table', '-t', default='', help="Table")
def dump(database, path, table):
    settings = import_settings(path)
    options = [
        '-c',       # --complete-insert
        '--skip-extended-insert',
    ]
    opts = ' '.join(options)
    CMD = 'mysqldump {OPTS} -u {USER} --password={PASSWORD} -h {HOST} {NAME} {TABLE}'
    print(CMD.format(TABLE=table, OPTS=opts, **settings.DATABASES[database]))


@db.command()
@click.option('--database', '-d', default='default')
@click.option('--path', '-p', default=None)
@click.option('--out', '-o', default=None, help="output directory")
def spy(database, path, out):
    # sudo apt-get install openjdk-8-jdk libmysql-java -y
    CONNECTOR = "/usr/share/java/mysql-connector-java.jar"      # UBUNTU    (TODO)
    settings = import_settings(path)
    OUT = out or settings.DATABASES[database]['NAME']
    JAR = bin_file('schemaspy.jar')
    SCRIPT = '''java -jar {JAR}  -t mysql -s {NAME} -o {OUT} -host {HOST} -db {NAME} -u {USER} -p {PASSWORD} -dp {CONNECTOR}'''
    click.echo(
        SCRIPT.format(JAR=JAR, CONNECTOR=CONNECTOR, OUT=OUT, **settings.DATABASES[database]))

def main():
    db()


if __name__ == '__main__':
    import_settings()
    main()
