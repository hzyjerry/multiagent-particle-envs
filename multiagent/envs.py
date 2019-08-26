import gym

def _make_env(scenario_name):
    from multiagent.environment import MultiAgentEnv
    import multiagent.scenarios as scenarios

    scenario = scenarios.load(scenario_name + ".py").Scenario()
    world = scenario.make_world()
    env = MultiAgentEnv(
        world, scenario.reset_world, scenario.reward, scenario.observation
    )
    return env



class MultiagentSimple(gym.Wrapper):
    def __init__(self):
        env = _make_env("simple")
        env.discrete_action_space = False
        super().__init__(env)


class MultiagentSimpleAdversary(gym.Wrapper):
    def __init__(self):
        env = _make_env("simple_adversary")
        super().__init__(env)


class MultiagentSimpleCrypto(gym.Wrapper):
    def __init__(self):
        env = _make_env("simple_crypto")
        super().__init__(env)


class MultiagentSimplePush(gym.Wrapper):
    def __init__(self):
        env = _make_env("simple_push")
        super().__init__(env)


class MultiagentSimpleSpread(gym.Wrapper):
    def __init__(self):
        env = _make_env("simple_spread")
        super().__init__(env)


class MultiagentSimpleTag(gym.Wrapper):
    def __init__(self):
        env = _make_env("simple_tag")
        super().__init__(env)


class MultiagentSimpleWorldComm(gym.Wrapper):
    def __init__(self):
        env = _make_env("simple_world_comm")
        super().__init__(env)


class MultiagentSimpleSpeakerListener(gym.Wrapper):
    def __init__(self):
        env = _make_env("simple_speaker_listener")
        super().__init__(env)
