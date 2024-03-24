BON2
====

A rewrite for Immibis's bearded-octo-nemesis for ForgeGradle by tterrag, with features by LexManos.

## Releases
- New releases available in the "[Releases](https://github.com/GTNewHorizons/BON2/releases)" section
- Old releases available on [tterrag's Jenkins](https://ci.tterrag.com/job/BON2/).

## Headless Mode Flags
- `--help` Prints this help menu and exits.
- `--version` Prints the version string and exits.
- `--inputJar` The jar file to deobfuscate. ***required***
- `--outputJar` The location and name of the output jar. Defaults to same dir and appends "-deobf".
- `--mcVer` Minecraft version number. ***required***
- `--mappingsVer` Mapping version, must be in the format channel_version. Example: stable_18-1.12.2 or snapshot_20191126-1.13, For convienance, the MC version can be excluded and --mcVer will be used. ***required***
- `--notch` Enables the full Notch names to MCP names mapping.
#### Example
`java -jar BON2-2.5.0.CUSTOM-all.jar --inputJar /some/file.jar --outputJar /some/other/file-deobf.jar --mcVer 1.7.10 --mappingsVer stable_12 --notch`
