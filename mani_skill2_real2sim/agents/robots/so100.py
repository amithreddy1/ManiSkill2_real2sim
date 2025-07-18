import numpy as np
import sapien.core as sapien
from sapien.core import Pose

from mani_skill2_real2sim.agents.base_agent import BaseAgent
from mani_skill2_real2sim.agents.configs.so100 import defaults 
from mani_skill2_real2sim.utils.sapien_utils import get_entity_by_name

class SO100(BaseAgent):
    _config: defaults.SO100DefaultConfig 

    """
        SO-100 5-DoF robot arm with 1-DoF gripper.
        This agent is configured via agents/configs/so100/defaults.py
    """

    @classmethod
    def get_default_config(cls):
        return defaults.SO100DefaultConfig() 

    def __init__(
        self, scene, control_freq, control_mode=None, fix_root_link=True, config=None
    ):
        if control_mode is None:
            control_mode = "arm_pd_ee_delta_pose_gripper_pd_joint_pos"
        super().__init__(
            scene,
            control_freq,
            control_mode=control_mode,
            fix_root_link=fix_root_link,
            config=config,
        )


    @property
    def base_pose(self):
        return self.robot.get_links()[0].get_pose()