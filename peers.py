#!/usr/bin/python

from charms.reactive import (
    hook,
    RelationBase,
)
from charms.reactive.bus import (
    StateList,
    State,
)
from charms.reactive import scopes


class LxdCluster(RelationBase):
    scope = scopes.SERVICE

    class states(StateList):
        connected = State('{relation_name}.connected')
        joined = State('{relation_name}.joined')
        departed = State('{relation_name}.departed')

    @hook('{peers:lxd-cluster}-relation-{joined,changed}')
    def peer_joined_or_changed(self):
        self.set_state('{relation_name}.connected')
        self.set_trigger_like_state(self.states.joined)

    @hook('{peers:lxd-cluster}-relation-departed')
    def peer_departed(self):
        self.set_trigger_like_state(self.states.departed)
        if not self.units():
            self.remove_state('{relation_name}.connected')
