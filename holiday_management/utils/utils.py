from autogen_agentchat.conditions import TextMentionTermination

# termination = TextMentionTermination("stop")

def get_termination_condition():
    """
    Get the termination condition for the agent.
    """
    TERMINATION_WORD = "stop"
    text_mention_termination = TextMentionTermination(TERMINATION_WORD)
    return text_mention_termination