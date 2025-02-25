// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Traceability {
    struct Event {
        uint256 id;
        string sensorId;
        uint256 timestamp;
        string details;
    }

    uint256 public eventCount;
    mapping(uint256 => Event) public events;

    event NewEvent(uint256 id, string sensorId, uint256 timestamp, string details);

    function recordEvent(string memory _sensorId, uint256 _timestamp, string memory _details) public {
        eventCount++;
        events[eventCount] = Event(eventCount, _sensorId, _timestamp, _details);
        emit NewEvent(eventCount, _sensorId, _timestamp, _details);
    }

    function getEvent(uint256 _id) public view returns (Event memory) {
        return events[_id];
    }
}
