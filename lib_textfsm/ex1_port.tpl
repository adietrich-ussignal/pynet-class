Value PORT_NAME (\S+)

Start
  ^Port.*Type\s*$$ -> ShowIntStatus

ShowIntStatus
  ^${PORT_NAME}\s+ -> Record

EOF
