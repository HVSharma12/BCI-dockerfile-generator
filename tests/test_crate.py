from bci_build.containercrate import ContainerCrate
from bci_build.package import BuildType
from bci_build.package import DevelopmentContainer
from bci_build.package import OsVersion

_BASE_KWARGS = {
    "name": "test",
    "package_name": "test-image",
    "pretty_name": "Test",
    "os_version": OsVersion.SP3,
    "package_list": ["sh"],
    "version": "1.0",
}


def test_multibuild_with_multi_flavor_docker():
    containers = [
        DevelopmentContainer(
            **_BASE_KWARGS,
            build_recipe_type=BuildType.DOCKER,
            build_flavor=flavor,
        )
        for flavor in ("flavor1", "flavor2")
    ]
    assert (
        ContainerCrate(containers).multibuild(containers[0])
        == """<multibuild>
    <package>flavor1</package>
    <package>flavor2</package>
</multibuild>"""
    )
