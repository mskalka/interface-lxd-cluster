#!/usr/bin/python

from charms.reactive import RelationBase
from charms.reactive import hook
from charms.reactive import scopes


class LxdCluster(RelationBase):

    scope = scopes.UNIT

    @hook('{peers:lxd-cluster}-relation-joined')
    def peers_joined(self):
        conv = self.conversation()
        conv.set_state('{relation_name}.joined')

    @hook('{peers:lxd-cluster}-relation-departed')
    def peers_departed(self):
        conv = self.conversation()
        conv.remove_state('{relation_name}.joined')
        conv.set_state('{relation_name}.departing')
