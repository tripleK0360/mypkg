import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():

    random = launch_ros.actions.Node(
        package='mypkg',
        executable='random',
        )
    listener = launch_ros.actions.Node(
        package='mypkg',
        executable='listener',
        output='screen'
        )

    return launch.LaunchDescription([random, listener])
