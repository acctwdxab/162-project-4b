# Dan Wu
# 1/26/2021
# 4b - Write a Box class whose init method takes three parameters and uses them to initialize the private length,
# width and height data members of a Box. It should also have a method named volume that returns the volume of the Box.
# It should have get methods named get_length, get_width, and get_height. Write a separate function named box_sort (not part of the Box class)
# that uses insertion sort to sort a list of Boxes from greatest volume to least volume.

class Box:
    """Box class whose init method takes three parameters length, width and height """
    def __init__(self,length,width,height):
       """initialize box with three private members """
       self._length = length
       self._width = width
       self._height = height

    def get_length(self) :
      """get length information of Box"""
      return self._length

    def get_width(self) :
       """get width information of Box"""
       return self._width

    def get_height(self):
        """get height measurement of Box"""
        return self._height


    def volume(self):
        """perform the calculation of volume using length, width and height"""
        return  self._length * self._width* self._height

def box_sort(list_of_boxes) :
      """uses insertion sort to sort a list of Boxes from greatest volume to least volume."""
      for i in range ( 1 , len ( list_of_boxes ) ) :
          box = list_of_boxes[i]
          j = i - 1;
          while j >= 0 and box < list_of_boxes[j] :
              list_of_boxes[j + 1] = list_of_boxes[j]
              j -= 1
              list_of_boxes[j + 1] = box

