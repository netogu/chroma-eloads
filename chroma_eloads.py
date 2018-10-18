

class chroma_63200:
    """Define Chroma 63200 Type Object."""

    def __init__(self, visa_resource):
        """Initialize eLoad Resource."""
        self.visa = visa_resource

    def load_off(self):
        """Turn eLoad OFF."""
        self.visa.write('load off')

    def load_on(self):
        """Turn eLoad ON."""
        self.visa.write('load on')

    def set_load_current(self, current_sp):
        """Set the load current."""
        self.visa.write('CURR:STAT:L1:{}'.format(current_sp))

    def read_load_current(self):
        """Read load current."""
        return float(self.visa.query('MEAS:CURR?'))

    def read_load_voltage(self):
        """Read load voltage."""
        return float(self.visa.query('MEAS:VOLT?'))

    def load_init(self):
        """Initialize the eLoad to its default state."""
        self.load_off()
