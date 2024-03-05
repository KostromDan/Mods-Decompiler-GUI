# MDG (Mods Decompiler Gui):

⚠️ WARNING ⚠️: Check license of all mods from mods folder or usage of this tool can be eligible and cause license
infringement.

## History and description:

The program is designed to simplify and make deobfuscation and decompilation of mods a one-click solution for everyone
interested.
In almost all English-speaking modding communities, the topic of decompilation is prohibited. If someone tries to
discuss decompilation and deobfuscation, ARR hamsters will immediately stop it. Since someone will be able to decompile
their paid mods and disrupt their profits. Although the majority (95%) those who are interested in this really need to
see how something works, find a bug, they are not going to decompile their paid mods in order to break the protection.
So it is almost impossible for a novice modder, and even more so for a modpackmaker, to learn how to do what this
program does. I want to overcome this and make sure that mods decompilation and deobfuscation can be used by any person,
who needs it, even those who only came to modding. A super intuitive one-click solution. You don't know how things work?
Just one click and you got your decomplied code!
This tool could save us hundreds of hours when developing modpacks or fixing conflicts in mods. For example, it has
already saved me around 30 hours. Instead of binary searching in mods, which takes a couple of hours, this program
allows us to find conflicts/problematic mod within 5 minutes.
If you don't know whether you need a specific option, use the builtin documentation. Every option is documented.
If you just want the code of your modpack to see how things work, simply don't modify the settings. The program will
already do what you need with default settings.
Program works by this algorithm; is some option disabled, it will be skipped:
deobfuscate -> decompile -> merge to mdk

## Usage cases:

* If you need to deobfuscate and/or decompile mod(s).
* If you want to get source code of whole your modpack with correct IDE indexing. Including source code mods, Minecraft
  and MnecraftForge.
    * Find which mod adds/breaks some thing/chat message.
    * See how things are implemented, understand their logic.

## Advantages:

* GUI. It's not console tool. It is easy and pleasant to use.
* It's all in one one-click complex solution.
* Builtin documentation. You can just press '?' and get help about any option.
* Despite other decompiler/deobf tools this is independent from apis. It uses mdk to deobf mods. So it won't break after
  mappings api changes like most of other deobf tools.

## Instruction:

1. Download the latest release of program from https://github.com/KostromDan/Mods-Decompiler-GUI/releases
2. Unzip archive
2. Run MDG.exe
3. Select mods folder and mdk.
4. Press start.
5. Done!

## Answers:

* Fabric version?
* * Maybe(if I will see many people need it). But tool already can be used for fabric mods. Forge mdk can deobfucate fabric mods, since mappings are same. The only thing you will miss is you can't see Fabric source code in merged mdk.
* Version range?
* * Any version where exist forge mdk and implemented fg.deobf().

## Screenshots:

### Main window:

![image](https://github.com/KostromDan/Mods-Decompiler-GUI/assets/90044015/bc6bcc45-3652-49ec-bb00-20c6e8b66397)

### Help(documentation) window:

![image](https://github.com/KostromDan/Mods-Decompiler-GUI/assets/90044015/b7ae85ce-0b03-45f0-a4a5-132d4f5c53d5)

### Progress window:

![image](https://github.com/KostromDan/Mods-Decompiler-GUI/assets/90044015/c455cc6a-ce64-4f71-81fc-4b6926e8f6a2)
