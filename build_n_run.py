"""Run tests for multiple Python versions concurrently."""
import sys

import anyio
import dagger


async def test():
    versions = ['3.10', '3.11']

    async with dagger.Connection(dagger.Config(log_output=sys.stderr)) as client:
        # get reference to the local project
        src = client.host().directory('.')

        async def test_version(version: str):
            python = (
                client.container().from_(f'python:{version}-slim-buster')
                # mount cloned repository into image
                .with_mounted_directory('/src', src)
                # set current working directory for next commands
                .with_workdir('/src')
                # install test dependencies
                .with_exec(['pip', 'install', '-r', 'requirements.txt'])
                # run tests
                .with_exec(['python', 'manage.py', 'test'])
            )

            print(f'Starting tests for Python {version}')

            # execute
            await python.exit_code()

            print(f'Tests for Python {version} succeeded!')

        # when this block exits, all tasks will be awaited (i.e., executed)
        async with anyio.create_task_group() as tg:
            for version in versions:
                tg.start_soon(test_version, version)

    print('All Test tasks have finished')


async def run_server():
    versions = ['3.10']

    async with dagger.Connection(dagger.Config(log_output=sys.stderr)) as client:
        # get reference to the local project
        src = client.host().directory('.')

        async def test_version(version: str):
            python = (
                client.container().from_(f'python:{version}-slim-buster')
                # mount cloned repository into image
                .with_mounted_directory('/src', src)
                # set current working directory for next commands
                .with_workdir('/src')
                # install test dependencies
                .with_exec(['pip', 'install', '-r', 'requirements.txt'])
                # run tests
                .with_exec(['make', 'start'])
            )

            print(f'Running Server for Python {version}')

            # execute

            await python.exit_code()

            print(f'Server for Python {version} started running!')

        # when this block exits, all tasks will be awaited (i.e., executed)
        async with anyio.create_task_group() as tg:
            for version in versions:
                tg.start_soon(test_version, version)

    print('All tasks have finished')


async def run():
    await test()
    await run_server()


if __name__ == '__main__':
    anyio.run(run)
