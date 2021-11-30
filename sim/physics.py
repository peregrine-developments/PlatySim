# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 13:11:44 2021

@author: Perry
"""

import math

from core.vector import *
from core.quaternion import *

@dataclass
class Rigidbody:
    """
    A class to represent a rigidbody object in three-dimensional space

    ...

    Attributes
    ----------
    mass : float
        Mass of the rigidbody (in kg)
    pos : Vector3
        Position of the rigidbody's CoG in space
    vel : Vector3
        Velocity of the rigidbody's CoG
    acc : Vector3
        Translational acceleration of the rigidbody's CoG
    gravity : bool
        Whether or not to apply gravity to this rigidbody
    ori : Vector3
        Vector3 representation of rotation of the rigidbody about its CoG
    oriQuat : Quaternion
        Quaternion representation of ori
    angularVel : Vector3
        Rotation of the rigidbody per second
    angularAcc : Vector3
        Rotational acceleration of the rigidbody per second
    
    Methods
    -------
    update():
        Updates a Rigidbody given a time difference
    applyForceCoM():
        Apply an inertial-frame force through the CoM of a Rgidbody
    applyForceCoMLocal():
        Apply a local-frame force through the CoM of a Rgidbody
    applyTorque():
        Apply an inertial-frame torque to a Rigidbody
    applyTorqueLocal():
        Apply a local-frame torque to a Rigidbody
    applyForce():
        Apply an inertial-frame force through a point on this Rigidbody
    applyForceLocal():
        Apply a local-frame force through a point on this Rigidbody
    """

    mass : float = 1
    moi : float = 1
    gravity : bool = True

    pos : Vector3 = Vector3.Zero()
    vel : Vector3 = Vector3.Zero()

    ori : Vector3 = Vector3.Zero()
    oriQuat : Quaternion = Quaternion.Zero()
    angularVel : Vector3 = Vector3.Zero()

    acc : Vector3 = Vector3.Zero()
    angularAcc : Vector3 = Vector3.Zero()

    def __init__(self, mass : float = 1, pos : Vector3 = Vector3(0, 0, 0), vel : Vector3 = Vector3(0, 0, 0), ori : Union[Vector3, Quaternion] = Vector3(0, 0, 0)) -> None:
        """
        Construct all necessary attributes for a Rigidbody object

        Parameters
        ----------
        mass : float
            Mass of the rigidbody (in kg)
        pos : Vector3
            Position of the rigidbody's CoG in space
        vel : Vector3
            Velocity of the rigidbody's CoG
        ori : Quaternion
            Rotation of the rigidbody about its CoG
        """

        self.mass = mass
        self.pos = pos
        self.vel = vel

        if isinstance(ori, Quaternion):
            self.ori = ori.ToAxisAngle()
        else:
            self.ori = ori
        self.oriQuat = Quaternion.FromAxisAngle(self.ori.norm(), self.ori.normalized())

    def update(self, dt : float) -> None:
        """
        Updates a Rigidbody given a time difference

        Parameters
        ----------
        dt : float
            Time difference for the update step
        """
        dt = float(dt)

        # TODO: Place all global constants (gravity, etc.) in a sim-wide settings class
        if self.gravity:
            self.acc += Vector3(0, 0, -9.807)

        self.vel += self.acc * dt
        self.pos += self.vel * dt

        self.angularVel += self.angularAcc * dt
        self.ori += self.angularVel * dt

        self.oriQuat = Quaternion.FromAxisAngle(self.ori.norm(), self.ori.normalized())

        # Reset acceleration every timestep so next forces/gravity work properly
        self.acc = Vector3.Zero()
        self.angularAcc = Vector3.Zero()

    def applyForceCoM(self, force : Vector3) -> None:
        """
        Apply an inertial-frame force through the CoM of a Rgidbody

        Parameters
        ----------
        force : Vector3
            The force (in Newtons) to apply to this Rigidbody
        """
        self.acc += force / float(self.mass)

    def applyForceCoMLocal(self, force : Vector3) -> None:
        """
        Apply a local-frame force through the CoM of a Rgidbody

        Parameters
        ----------
        force : Vector3
            The force (in Newtons) to apply to this Rigidbody
        """
        inertialForce = force * self.oriQuat
        self.applyForceCoM(inertialForce)

    def applyTorque(self, torque : Vector3) -> None:
        """
        Apply an inertial-frame torque to a Rigidbody

        Parameters
        ----------
        torque : Vector3
            The torque (in Newton-meters) to apply to this Rigidbody
        """
        self.angularAcc += torque / float(self.moi)

    def applyTorqueLocal(self, torque : Vector3) -> None:
        """
        Apply a local-frame torque to a Rigidbody

        Parameters
        ----------
        torque : Vector3
            The torque (in Newton-meters) to apply to this Rigidbody
        """
        inertialTorque = torque * self.oriQuat
        self.applyTorque(inertialTorque)

    def applyForce(self, force : Vector3, dis : Vector3) -> None:
        """
        Apply an inertial-frame force through a point on this Rigidbody

        Parameters
        ----------
        force : Vector3
            The force (in Newtons) to apply to this Rigidbody
        dis : Vector3
            The displacement (in meters) of the point to which the force is applied
        """
        torque = dis.cross(force)
        self.applyForceCoM(force)
        self.applyTorque(torque)

    def applyForceLocal(self, force : Vector3, dis : Vector3) -> None:
        """
        Apply a local-frame force through a point on this Rigidbody

        Parameters
        ----------
        force : Vector3
            The force (in Newtons) to apply to this Rigidbody
        dis : Vector3
            The displacement (in meters) of the point to which the force is applied
        """
        inertialForce = force * self.oriQuat
        inertialDis = dis * self.oriQuat
        self.applyForce(inertialForce, inertialDis)

    