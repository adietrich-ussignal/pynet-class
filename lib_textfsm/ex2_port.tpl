Value PORT_NAME (\S+)
Value STATUS (\S+)
Value VLAN (\d{1,4})
Value DUPLEX (\S+)
Value SPEED (\S+)
Value TYPE (\S+)


Start
  ^Port.*Type\s*$$ -> ShowIntStatus

ShowIntStatus
  ^${PORT_NAME}\s+${STATUS}\s+${VLAN}\s+${DUPLEX}\s+${SPEED}\s+${TYPE}\s*$$ -> Record

EOF
