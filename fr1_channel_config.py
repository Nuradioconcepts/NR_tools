import tkinter as tk

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # Labels
        self.label_frequency = tk.Label(master, text="SSB Frequency (MHz):")
        self.label_spacing = tk.Label(master, text="Subcarrier Spacing (kHz):")
        self.label_bandwidth = tk.Label(master, text="Carrier Bandwidth (MHz):")
        self.label_offset_ssb = tk.Label(master, text="SSB Subcarrier Offset:")
        self.label_offset_a = tk.Label(master, text="Offset to Point A:")

        self.label_resource_block = tk.Label(master, text="Resource Block Size (MHz):")
        self.label_ssb_size = tk.Label(master, text="SSB Size (MHz):")
        self.label_ssb_start = tk.Label(master, text="SSB Start (MHz):")
        self.label_point_a_offset = tk.Label(master, text="Point A Offset (MHz):")
        self.label_subcarrier_offset = tk.Label(master, text="Subcarrier Offset (MHz):")
        self.label_point_a = tk.Label(master, text="Point A (MHz):")
        self.label_bandwidth_out = tk.Label(master, text="Bandwidth (MHz):")
        self.label_carrier_center = tk.Label(master, text="Carrier Center (MHz):")

        # Entries
        self.entry_frequency = tk.Entry(master)
        self.entry_spacing = tk.Entry(master)
        self.entry_bandwidth = tk.Entry(master)
        self.entry_offset_ssb = tk.Entry(master)
        self.entry_offset_a = tk.Entry(master)

        # Buttons
        self.calculate_button = tk.Button(master, text="Calculate", command=self.calculate)

        # Grid layout
        self.label_frequency.grid(row=0, column=0, sticky="e")
        self.label_spacing.grid(row=1, column=0, sticky="e")
        self.label_bandwidth.grid(row=2, column=0, sticky="e")
        self.label_offset_ssb.grid(row=3, column=0, sticky="e")
        self.label_offset_a.grid(row=4, column=0, sticky="e")

        self.entry_frequency.grid(row=0, column=1)
        self.entry_spacing.grid(row=1, column=1)
        self.entry_bandwidth.grid(row=2, column=1)
        self.entry_offset_ssb.grid(row=3, column=1)
        self.entry_offset_a.grid(row=4, column=1)

        self.calculate_button.grid(row=5, columnspan=2)

        self.label_resource_block.grid(row=6, column=0, sticky="e")
        self.label_ssb_size.grid(row=7, column=0, sticky="e")
        self.label_ssb_start.grid(row=8, column=0, sticky="e")
        self.label_point_a_offset.grid(row=9, column=0, sticky="e")
        self.label_subcarrier_offset.grid(row=10, column=0, sticky="e")
        self.label_point_a.grid(row=11, column=0, sticky="e")
        self.label_bandwidth_out.grid(row=12, column=0, sticky="e")
        self.label_carrier_center.grid(row=13, column=0, sticky="e")

    def calculate(self):
        frequency = float(self.entry_frequency.get())
        spacing = float(self.entry_spacing.get()) / 1000  # Convert kHz to MHz
        bandwidth = float(self.entry_bandwidth.get())
        offset_ssb = float(self.entry_offset_ssb.get())
        offset_a = float(self.entry_offset_a.get())

        resource_block_size = spacing * 12
        ssb_size = resource_block_size * 20
        ssb_start = frequency - (ssb_size / 2)
        point_a_offset = offset_a * 0.18  # Convert MHz to kHz
        subcarrier_offset = offset_ssb * 0.015  # Convert MHz to kHz
        point_a = ssb_start - (point_a_offset + subcarrier_offset)
        bandwidth_out = bandwidth * resource_block_size
        carrier_center = point_a + (bandwidth_out / 2)

        # Output results
        self.label_resource_block.config(text=f"Resource Block Size: {resource_block_size:.2f} MHz")
        self.label_ssb_size.config(text=f"SSB Size: {ssb_size:.2f} MHz")
        self.label_ssb_start.config(text=f"SSB Start: {ssb_start:.2f} MHz")
        self.label_point_a_offset.config(text=f"Point A Offset: {point_a_offset:.2f} MHz")
        self.label_subcarrier_offset.config(text=f"Subcarrier Offset: {subcarrier_offset:.2f} MHz")
        self.label_point_a.config(text=f"Point A: {point_a:.2f} MHz")
        self.label_bandwidth_out.config(text=f"Bandwidth: {bandwidth_out:.2f} MHz")
        self.label_carrier_center.config(text=f"Carrier Center: {carrier_center:.2f} MHz")

root = tk.Tk()
app = CalculatorApp(root)
root.mainloop()
