from package import Package

class StandardPackage(Package):
  """
  Class used to represent a Package
  """

  def __init__(self, id_package: int = 0, weight: float = 0.5 , description: str = "DescriptionOfProduct" , cost: float = 1.5, fixed_fee: float = 1.0):
    """ standard package constructor object.

    :param fixed_fee: fixed_fee of standard package.
    :type fixed_fee: float
    :returns: StandardPackage Package.
    :rtype: Package
    """
    super().__init__(id_package, weight, description, cost)
  
    self._fixed_fee = fixed_fee
  
  @property
  def fixed_fee(self) -> float:
    return self._fixed_fee
  
  @fixed_fee.setter
  def fixed_fee(self, fixed_fee: float):
    """ The fixed_fee of the standard package.
    :param fixed_fee: fixed_fee of standard package.
    :type: float
    """
    self._fixed_fee = fixed_fee

  def calculate(self):
    print(f"The shipping cost by adding the fixed fee at the cost based on the weight of the package " f"is ${(self._fixed_fee + self._weight ) * self._cost}")
  
  def __str__(self):
    """ Returns str of package.
    :returns: sting package
    :rtype: str
    """
    return '({0}'.format(self.fixed_fee)
  
  