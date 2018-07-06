#!/usr/bin/env python
# encoding: utf-8
'''
XML2Dict: Convert xml string to python dict

@author: Mc.Spring
@contact: Heresy.Mc@gmail.com
@since: Created on 2009-5-18
@todo: Add namespace support
@copyright: Copyright (C) 2009 MC.Spring Team. All rights reserved.
@license: http://www.apache.org/licenses/LICENSE-2.0 Apache License
'''

try:
    import xml.etree.ElementTree as ET
except:
    import cElementTree as ET # for 2.4


__all__ = ['XML2Dict']


class XML2Dict(object):

    def __init__(self, coding='UTF-8'):
        self._coding = coding

    def _parse_node(self, node):
        tree = {}

        #Save childrens
        for child in node.getchildren():
            print("new child", child.tag, child.attrib, child.text)
            ctag = child.tag
            cattr = child.attrib
            ctext = child.text.strip().encode(self._coding) if child.text is not None else ''
            ctree = self._parse_node(child)

            if not ctree:
                cdict = self._make_dict(ctag, ctext, cattr)
            else:
                cdict = self._make_dict(ctag, ctree, cattr)

            if ctag not in tree: # First time found
                tree.update(cdict)
                continue

            atag = '@' + ctag
            atree = tree[ctag]
            if not isinstance(atree, list):
                if not isinstance(atree, dict):
                    atree = {}

                if atag in tree:
                    atree['#'+ctag] = tree[atag]
                    del tree[atag]

                tree[ctag] = [atree] # Multi entries, change to list

            if cattr:
                ctree['#'+ctag] = cattr


            tree[ctag].append(ctree)

        return  tree


    def parse_node(self, node):
        tree = {}
        for child in node:
            #print("child tag", child.tag, "child.attrib", child.attrib )
            #print type(child.attrib)
            #for k, v in child.attrib.items():
            #    print(k, v)
            child_tree = self.parse_node(child)
            tree[child.tag] = child_tree
        print(tree)
        return tree

    def _make_dict(self, tag, value, attr=None):
        '''Generate a new dict with tag and value

        If attr is not None then convert tag name to @tag
        and convert tuple list to dict
        '''
        ret = {tag: value}

        # Save attributes as @tag value
        if attr:
            atag = '@' + tag

            aattr = {}
            for k, v in attr.items():
                aattr[k] = v

            ret[atag] = aattr

            del atag
            del aattr

        return ret


    def parse(self, path):
        data = open(path).read()
        EL = ET.fromstring(data)
        self._make_dict(EL.tag, self._parse_node(EL), EL.attrib)




