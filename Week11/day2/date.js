const readline = require('readline');
const Holidays = require('date-holidays');

function timeUntilJan1() {
    const currentDate = new Date();
    const firstJan = new Date(currentDate.getFullYear() + 1, 0, 1);
    const timeLeft = firstJan - currentDate;
  
    const days = Math.floor(timeLeft / (1000 * 60 * 60 * 24));
    const hours = Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((timeLeft % (1000 * 60)) / 1000);
      return {
      days,
      hours,
      minutes,
      seconds
    };
  }

function timelived(year, month, day){
    let currentDate = new Date();
    const birthdate = new Date(year, month - 1, day);
    let time = currentDate - birthdate
    const minutes = Math.floor(time / (1000 * 60));
    return {
        minutes,
      };
      }

function timeUntilHoliday(){
    const hd = new Holidays('US');
    currentDate = new Date();
    const holidays = hd.getHolidays(currentDate.getFullYear());
    holidays.sort((a, b) => a.date.getTime() - b.date.getTime());

    let nearestHoliday;
    for (const holiday of holidays) {
      if (holiday.date > currentDate) {
        nearestHoliday = holiday;
        break;
      }
    }
    if (nearestHoliday) {
        // Calculate the time until the nearest holiday
        const timeUntilHoliday = nearestHoliday.date.getTime() - currentDate.getTime();
        const daysUntilHoliday = Math.ceil(timeUntilHoliday / (1000 * 60 * 60 * 24));
    
        console.log('Nearest holiday:');
        console.log(nearestHoliday.name);
        console.log('Days until the holiday:', daysUntilHoliday);
      } else {
        console.log('No upcoming holidays found.');
      }
    }    

timeUntilHoliday()
  module.exports = {timeUntilJan1, timelived}