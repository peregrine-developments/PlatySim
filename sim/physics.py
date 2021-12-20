# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 13:11:44 2021

@author: Perry
"""

import math

from core.vector import *
from core.quaternion import *

from typing import Callable

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
    gravity : bool = True

    pos : Vector3 = Vector3.Zero()
    vel : Vector3 = Vector3.Zero()
    acc : Vector3 = Vector3.Zero()

    lastAcc : Vector3 = Vector3.Zero()

    moi : Vector3 = Vector3(1, 1, 1)

    ori : Quaternion = Quaternion.Zero()
    spin : Quaternion = Quaternion.Zero()
    angularVel : Vector3 = Vector3.Zero()
    angularAcc : Vector3 = Vector3.Zero()


    def __init__(self, mass : float = 1, moi : Union[float, Vector3] = 1, gravity : bool = True, pos : Vector3 = Vector3(0, 0, 0), vel : Vector3 = Vector3(0, 0, 0), ori : Quaternion = Quaternion.Zero()) -> None:
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

        self.mass = float(mass)

        self.pos = pos
        self.vel = vel

        if isinstance(moi, Vector3):
            self.moi = moi
        else:
            self.moi = Vector3(moi, moi, moi)
        
        self.ori = ori

        self.gravity = gravity

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
        
        self.ori *= Quaternion.FromRotationVector(self.angularVel * dt)

        # Reset acceleration every timestep so next forces/gravity work properly
        self.lastAcc = self.acc
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
        globalForce = force * self.ori
        self.applyForceCoM(globalForce)

    def applyTorque(self, torque : Vector3) -> None:
        """
        Apply an inertial-frame torque to a Rigidbody

        Parameters
        ----------
        torque : Vector3
            The torque (in Newton-meters) to apply to this Rigidbody
        """
        torqueAcc = Vector3(torque.x / self.moi.x, torque.y / self.moi.y, torque.z / self.moi.z)
        self.angularAcc += torqueAcc

    def applyTorqueLocal(self, torque : Vector3) -> None:
        """
        Apply a local-frame torque to a Rigidbody

        Parameters
        ----------
        torque : Vector3
            The torque (in Newton-meters) to apply to this Rigidbody
        """
        globalTorque = torque * self.ori
        self.applyTorque(globalTorque)

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
        globalForce = force * self.ori
        globalDis = dis * self.ori
        self.applyForce(globalForce, globalDis)

    def applyGlobalForceLocal(self, force : Vector3, dis : Vector3) -> None:
        """
        Apply a global-frame force through a point on this Rigidbody

        Parameters
        ----------
        force : Vector3
            The force (in Newtons) to apply to this Rigidbody
        dis : Vector3
            The displacement (in meters) of the point to which the force is applied
        """
        globalDis = dis * self.ori
        self.applyForce(force, globalDis)

@dataclass
class AerodynamicRigidbody(Rigidbody):
    """
    A rigidbody with aerodynamic properties.

    Attributes
    ----------
    dragCoeff : Callable[[float], float] -> float
        The function that relates angle of attack to drag coefficient
    liftCoeff : Callable[[float], float] -> float
        The function that relates angle of attack to lift coefficient
    dragArea : float
        The reference area on which Cd is applied
    liftArea : float
        The reference area on which Cl is applied
    centerOfPressure : Vector3
        The local frame offset of the CoP from the CoM
    """

    dragCoeff : Callable[[float], float] = lambda aoa : 0
    liftCoeff : Callable[[float], float] = lambda aoa : 0
    dragArea : float = 1
    liftArea : float = 1
    centerOfPressure : Vector3 = Vector3.Zero()

    globalWind : Vector3 = Vector3.Zero()
    airDensity : float = 1.225

    def __init__(self, mass : float = 1, moi : Union[float, Vector3] = 1, gravity : bool = True, pos : Vector3 = Vector3(0, 0, 0), vel : Vector3 = Vector3(0, 0, 0), ori : Quaternion = Quaternion.Zero(),
                dragCoeff : Callable[[float], float] = lambda aoa : 0, liftCoeff : Callable[[float], float] = lambda aoa : 0, dragArea : float = 1, liftArea : float = 1, centerOfPressure : Vector3 = Vector3.Zero()) -> None:
        """
        Construct all necessary attributes for a Rigidbody object

        Parameters
        ----------
        ALL RIGIDBODY VALUES HERE
        dragCoeff : Callable[[float], float] -> float
            The function that relates angle of attack to drag coefficient
        liftCoeff : Callable[[float], float] -> float
            The function that relates angle of attack to lift coefficient
        dragArea : float
            The reference area on which Cd is applied
        liftArea : float
            The reference area on which Cl is applied
        centerOfPressure : Vector3
            The local frame offset of the CoP from the CoM
        """

        super().__init__(mass, moi, gravity, pos, vel, ori)

        self.dragCoeff = dragCoeff
        self.liftCoeff = liftCoeff
        self.dragArea = dragArea
        self.liftArea = liftArea
        self.centerOfPressure = centerOfPressure

    def setWind(self, wind : Vector3) -> None:
        """
        Set the global wind vector

        Parameters
        ----------
        wind : Vector3
            The global wind vector
        """
        self.globalWind = wind

    def update(self, dt : float) -> None:
        """
        Updates a Rigidbody given a time difference

        Parameters
        ----------
        dt : float
            Time difference for the update step
        """
        dt = float(dt)

        # Calculate the velocity relative to the wind
        velRelWind = self.vel - self.globalWind

        # Calculate the angle of attack
        aoa = velRelWind.angle(Vector3.UnitZ())

        # Calculate the drag and lift coefficients
        dragCoeff = self.dragCoeff(aoa)
        liftCoeff = self.liftCoeff(aoa)

        # Calculate the drag and lift forces
        dragForce = -velRelWind.normalized() * dragCoeff * self.dragArea * self.airDensity * velRelWind.norm() * velRelWind.norm() * 0.5
        liftForce = Vector3.Zero()

        # Apply the forces globally with local offset
        self.applyGlobalForceLocal(dragForce, self.centerOfPressure)
        self.applyGlobalForceLocal(liftForce, self.centerOfPressure)

        super().update(dt)
