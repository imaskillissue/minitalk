/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   client.h                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ekarpawi <ekarpawi@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/12/15 16:35:53 by ekarpawi          #+#    #+#             */
/*   Updated: 2023/12/15 16:35:53 by ekarpawi         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#pragma once
#include "libft/libft.h"
#include "libft/bit_manipulation.h"

void	send_message(int pid, char *message);
void	send_char(int pid, char c);