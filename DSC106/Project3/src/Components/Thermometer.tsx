import { useEffect, useRef } from "react";
import * as d3 from "d3";

interface ThermometerProps {
  temp: number;
  gender: "male" | "female";
}

const Thermometer = ({ temp, gender }: ThermometerProps) => {
  const maxTemp = 39;
  const minTemp = 35;
  const svgRef = useRef<SVGSVGElement | null>(null);

  useEffect(() => {
    const svg = d3.select(svgRef.current);
    svg.selectAll("*").remove();

    const baseColor = gender === "female" ? "#FF69B4" : "#4169E1";

    // Create the thermometer structure
    svg
      .append("rect")
      .attr("x", 40)
      .attr("y", 30)
      .attr("width", 20)
      .attr("height", 200)
      .attr("fill", "#ccc")
      .attr("rx", 10)
      .attr("ry", 10);

    // Thermometer bulb
    svg.append("circle").attr("cx", 50).attr("cy", 230).attr("r", 15).attr("fill", "#ccc");

    // Calculate the fill height based on temp
    const fillHeight = Math.min(Math.max((200 * (temp - minTemp)) / (maxTemp - minTemp), 0), 200);

    // Temperature Fill
    svg
      .append("rect")
      .attr("x", 40)
      .attr("y", 230 - fillHeight)
      .attr("width", 20)
      .attr("height", fillHeight)
      .attr("fill", baseColor)
      .attr("rx", 10)
      .attr("ry", 10);

    // Fill for the bulb
    svg
      .append("circle")
      .attr("cx", 50)
      .attr("cy", 230)
      .attr("r", 20)
      .attr("fill", baseColor);
  }, [temp, gender]);

  return (
    <div className="flex flex-col items-center">
      <svg ref={svgRef} width={100} height={300} />
      <h3 className="text-xl font-bold">{Math.round(temp * 100) / 100}°C</h3>
    </div>
  );
};

export default Thermometer;
