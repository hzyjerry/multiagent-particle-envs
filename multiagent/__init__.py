from gym.envs.registration import register



# Multiagent envs
# ----------------------------------------

register(
    id="MultiagentSimple-v0",
    entry_point="multiagent.envs:MultiagentSimple",
    max_episode_steps=100,
)

register(
    id="MultiagentSimpleAdversary-v0",
    entry_point="multiagent.envs:MultiagentSimpleAdversary",
    max_episode_steps=100,
)

register(
    id="MultiagentSimpleCrypto-v0",
    entry_point="multiagent.envs:MultiagentSimpleCrypto",
    max_episode_steps=100,
)

register(
    id="MultiagentSimplePush-v0",
    entry_point="multiagent.envs:MultiagentSimplePush",
    max_episode_steps=100,
)

register(
    id="MultiagentSimpleSpread-v0",
    entry_point="multiagent.envs:MultiagentSimpleSpread",
    max_episode_steps=100,
)

register(
    id="MultiagentSimpleTag-v0",
    entry_point="multiagent.envs:MultiagentSimpleTag",
    max_episode_steps=100,
)

register(
    id="MultiagentSimpleWorldComm-v0",
    entry_point="multiagent.envs:MultiagentSimpleWorldComm",
    max_episode_steps=100,
)

register(
    id="MultiagentSimpleSpeakerListener-v0",
    entry_point="multiagent.envs:MultiagentSimpleSpeakerListener",
    max_episode_steps=100,
)