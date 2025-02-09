$(document).ready(function() {
    const walkthrough = {
      index: 0,
  
      nextScreen: function() {
        if (this.index < this.indexMax()) {
          this.index++;
          this.updateScreen();
        }
      },
  
      prevScreen: function() {
        if (this.index > 0) {
          this.index--;
          this.updateScreen();
        }
      },
  
      updateScreen: function() {
        this.reset();
        this.goTo(this.index);
        this.setBtns();
      },
  
      setBtns: function() {
        const $nextBtn = $('.next-screen');
        const $prevBtn = $('.prev-screen');
        const $lastBtn = $('.finish');
        
        if (this.index === this.indexMax()) {
          $nextBtn.prop('disabled', true);
          $prevBtn.prop('disabled', false);
          $lastBtn.addClass('active').prop('disabled', false);
        } else if (this.index === 0) {
          $nextBtn.prop('disabled', false);
          $prevBtn.prop('disabled', true);
          $lastBtn.removeClass('active').prop('disabled', true);
        } else {
          $nextBtn.prop('disabled', false);
          $prevBtn.prop('disabled', false);
          $lastBtn.removeClass('active').prop('disabled', true);
        }
      },
  
      goTo: function(index) {
        $('.screen').eq(index).addClass('active');
        $('.dot').eq(index).addClass('active');
      },
  
      reset: function() {
        $('.screen, .dot').removeClass('active');
      },
  
      indexMax: function() {
        return $('.screen').length - 1;
      },
  
      closeModal: function() {
        $('.walkthrough, .shade').removeClass('reveal');
        setTimeout(() => {
          $('.walkthrough, .shade').removeClass('show');
          this.index = 0;
          this.updateScreen();
        }, 200);
      },
  
      openModal: function() {
        $('.walkthrough, .shade').addClass('show');
        setTimeout(() => {
          $('.walkthrough, .shade').addClass('reveal');
        }, 200);
        this.updateScreen();
      }
    };
  
    $('.next-screen').click(function() {
      walkthrough.nextScreen();
    });
  
    $('.prev-screen').click(function() {
      walkthrough.prevScreen();
    });
  
    $('.close').click(function() {
      walkthrough.closeModal();
    });
  
    $('.open-walkthrough').click(function() {
      walkthrough.openModal();
    });
  
    walkthrough.openModal();
  
    // Optionally use arrow keys to navigate walkthrough
    $(document).keydown(function(e) {
      switch (e.which) {
        case 37: // left arrow
          walkthrough.prevScreen();
          break;
        case 38: // up arrow
          walkthrough.openModal();
          break;
        case 39: // right arrow
          walkthrough.nextScreen();
          break;
        case 40: // down arrow
          walkthrough.closeModal();
          break;
        default:
          return;
      }
      e.preventDefault();
    });
  });
