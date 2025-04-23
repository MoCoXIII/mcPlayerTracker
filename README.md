# Intentions
This program is meant for converging onto Minecraft players' location based on if they appear behind the colon (:) of the /msg return message.

Note that the target player needs to stand still while the program is executing. In addition to that, always stay with the same target player, from beginning to end of execution, or else the execution might never end.

# WARNING
The program takes full control of your keyboard. Keep that in mind while executing. All of your keyboard actions will be suppressed during execution.

# Usage
This program was only tested on Minecraft Bedrock Edition.

Starting your Minecraft instance before execution of this script is recommended.

After starting the program, open your Minecraft instance. Make sure to not press "s" during this phase. Once you are **inside** the Minecraft chat, press "s" to start. It will take a second to paste and execute a /msg command, before opening the chat again by itself. Your job is now picking your target player from the player list after the colon (:) and clicking "c" if their name appears in the list. If it does not, press "d". The search area should either expand and search again, or if you have already clicked "c" at least once, refine the coordinates of our guess. Once the program is sure to be within "precision_threshold" blocks of your target in all directions, it will halt.

# Modification
The only modifications you need to make as a user are\
setting the **precision_threshold >= 1** to trade accuracy for a lower number of operations\
and\
setting **b >= 1** to decrease the number of operations if you know roughly how far your target is away.\
Keeping it at 1 will consume more operations to scale up your search if the target is far away.